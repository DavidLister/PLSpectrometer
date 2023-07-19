# graphing.py
#
# Graphs for GUI
# Created by Elliot Wadge
# Edited by Alistair Bevan
# July 2023
#

import sys
from typing import List
from miscellaneous import find_minimum
import numpy as np
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch
from PyQt5.QtChart import QChart, QLineSeries, QSplineSeries
from PyQt5.QtCore import QPointF, QRect, QRectF, QSizeF, Qt
from PyQt5.QtGui import QColor, QFont, QFontMetrics, QMouseEvent, QPainter, QPainterPath, QResizeEvent
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsSceneMouseEvent, \
    QGraphicsSimpleTextItem, QGraphicsView, QStyleOptionGraphicsItem, QWidget

# This is the little messageBox (Elliot didn't make this, he found it on the internet)
class Callout(QGraphicsItem):

    def __init__(self, parent: QChart):
        super().__init__()
        self.m_chart: QChart = parent
        self.m_text: str = ''
        self.m_anchor: QPointF = QPointF()
        self.m_font: QFont = QFont()
        self.m_textRect: QRectF = QRectF()
        self.m_rect: QRectF = QRectF()

    def setText(self, text: str):
        self.m_text = text
        metrics = QFontMetrics(self.m_font)
        self.m_textRect = QRectF(metrics.boundingRect(QRect(0, 0, 150, 150), Qt.AlignLeft, self.m_text))
        self.m_textRect.translate(5, 5)
        self.prepareGeometryChange()
        self.m_rect = QRectF(self.m_textRect.adjusted(-5, -5, 5, 5))
        self.updateGeometry()

    def updateGeometry(self):
        self.prepareGeometryChange()
        self.setPos(self.m_chart.mapToPosition(self.m_anchor) + QPointF(10, -50))

    def boundingRect(self) -> QRectF:
        from_parent = self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor))
        anchor = QPointF(from_parent)
        rect = QRectF()
        rect.setLeft(min(self.m_rect.left(), anchor.x()))
        rect.setRight(max(self.m_rect.right(), anchor.x()))
        rect.setTop(min(self.m_rect.top(), anchor.y()))
        rect.setBottom(max(self.m_rect.bottom(), anchor.y()))
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        path = QPainterPath()
        mr = self.m_rect
        path.addRoundedRect(mr, 5, 5)

        anchor = QPointF(self.mapFromParent(self.m_chart.mapToPosition(self.m_anchor)))
        if not mr.contains(anchor):
            point1 = QPointF()
            point2 = QPointF()

            # Establish the position of the anchor point in relation to self.m_rect
            above = anchor.y() <= mr.top()
            above_center = mr.top() < anchor.y() <= mr.center().y()
            below_center = mr.center().y() < anchor.y() <= mr.bottom()
            below = anchor.y() > mr.bottom()

            on_left = anchor.x() <= mr.left()
            left_of_center = mr.left() < anchor.x() <= mr.center().x()
            right_of_center = mr.center().x() < anchor.x() <= mr.right()
            on_right = anchor.x() > mr.right()

            # get the nearest self.m_rect corner.
            x = (on_right + right_of_center) * mr.width()
            y = (below + below_center) * mr.height()
            corner_case = (above and on_left) or (above and on_right) or (below and on_left) or (below and on_right)
            vertical = abs(anchor.x() - x) > abs(anchor.y() - y)
            horizontal = bool(not vertical)

            x1 = x + left_of_center * 10 - right_of_center * 20 + corner_case * horizontal * (
                    on_left * 10 - on_right * 20)
            y1 = y + above_center * 10 - below_center * 20 + corner_case * vertical * (above * 10 - below * 20)
            point1.setX(x1)
            point1.setY(y1)

            x2 = x + left_of_center * 20 - right_of_center * 10 + corner_case * horizontal * (
                    on_left * 20 - on_right * 10)
            y2 = y + above_center * 20 - below_center * 10 + corner_case * vertical * (above * 20 - below * 10)
            point2.setX(x2)
            point2.setY(y2)

            path.moveTo(point1)
            path.lineTo(anchor)
            path.lineTo(point2)
            path = path.simplified()

        painter.setPen(QColor(30, 30, 30))
        painter.setBrush(QColor(255, 255, 255))
        painter.drawPath(path)
        painter.drawText(self.m_textRect, self.m_text)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        event.setAccepted(True)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        if event.buttons() & Qt.LeftButton:
            self.setPos(self.mapToParent(event.pos() - event.buttonDownPos(Qt.LeftButton)))
            event.setAccepted(True)
        else:
            event.setAccepted(False)


class View(QGraphicsView):

    max = 10

    def __init__(self, parent=None, name = '', log = False):
        '''configures the plot'''
        super().__init__(parent)
        self.m_callouts: List[Callout] = []
        self.setDragMode(QGraphicsView.NoDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.log = log
        # chart
        self.m_chart = QChart(parent)
        self.m_chart.setMinimumSize(640, 480)
        self.m_chart.setTitle(name)
        self.m_chart.legend().hide()
        self.series = QLineSeries()
        self.m_chart.addSeries(self.series)
        self.m_chart.createDefaultAxes()
        self.m_chart.setAcceptHoverEvents(True)
        self.m_chart.setTheme(qtch.QChart.ChartThemeDark)
        self.m_chart.setCursor(qtg.QCursor(qtc.Qt.CrossCursor))
        self.xdata = []
        self.ydata = []
        self.setRenderHint(QPainter.Antialiasing)

        self.setScene(QGraphicsScene())
        self.scene().addItem(self.m_chart)

        self.m_coordX = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 30)
        self.m_coordX.setBrush(qtg.QColor('green'))
        self.m_coordX.setText("X: ")
        self.m_coordY = QGraphicsSimpleTextItem(self.m_chart)
        self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 30)
        self.m_coordY.setBrush(qtg.QColor('green'))
        self.m_coordY.setText("Y: ")

        self.x_axis = qtch.QValueAxis()
        self.x_axis.setRange(0, 10)
        self.rangeX = 10

        if self.log:
            self.y_axis = qtch.QLogValueAxis()
            self.y_axis.setBase(10)
            self.y_axis.setRange(1,self.max);
        else:
            self.y_axis = qtch.QValueAxis()
            self.y_axis.setRange(0,self.max)

        self.m_chart.setAxisX(self.x_axis,self.series)
        self.m_chart.setAxisY(self.y_axis,self.series)

        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)
        self.m_tooltip.hide()
        self.series.hovered.connect(self.tooltip)
        self.setMouseTracking(True)

    def resizeEvent(self, event: QResizeEvent):
        '''how to handle resizing'''
        if scene := self.scene():
            scene.setSceneRect(QRectF(QPointF(0, 0), QSizeF(event.size())))
            self.m_chart.resize(QSizeF(event.size()))
            self.m_coordX.setPos(self.m_chart.size().width() / 2 - 50, self.m_chart.size().height() - 30)
            self.m_coordY.setPos(self.m_chart.size().width() / 2 + 50, self.m_chart.size().height() - 30)

            for callout in self.m_callouts:
                callout.updateGeometry()

        super().resizeEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        '''update the display at the bottom of graph with mouse movement'''
        from_chart = self.m_chart.mapToValue(event.pos())
        self.m_coordX.setText(f"X: {from_chart.x():.3f}")
        self.m_coordY.setText(f"Y: {from_chart.y():.3f}")
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        '''add callouts and delete them with left and right clicks'''
        if event.buttons() & Qt.LeftButton & self.m_tooltip.isVisible():
            self.keep_callout()
            event.setAccepted(True)

        elif event.buttons() & Qt.RightButton:
            self.remove_callout()
            event.setAccepted(True)

        else:
            event.setAccepted(False)



    #draws the little boxes that show the point value
    def tooltip(self, point: QPointF, state: bool):
        if not self.m_tooltip:
            self.m_tooltip = Callout(self.m_chart)

        if state:
            #normalize the axis not perfect since the aspect ratio is not square
            arr_x = np.array(self.xdata)/self.rangeX
            arr_y = np.array(self.ydata)/self.max
            min_i = find_minimum(arr_x, arr_y, point.x()/self.rangeX, point.y()/self.max)
            self.m_tooltip.setText(f"X: {self.xdata[min_i]:.3f} \nY: {self.ydata[min_i]:.3f} ")
            self.m_tooltip.m_anchor = QPointF(self.xdata[min_i],self.ydata[min_i])
            self.m_tooltip.setZValue(11)
            self.m_tooltip.updateGeometry()
            self.m_tooltip.show()
        else:
            self.m_tooltip.hide()

    #pins the callout to the chart
    def keep_callout(self):
        self.m_callouts.append(self.m_tooltip)
        self.m_tooltip = Callout(self.m_chart)
        self.scene().addItem(self.m_tooltip)
        self.m_tooltip.hide()

    #removes the last pinned callout
    def remove_callout(self):
        if len(self.m_callouts) != 0:
            self.scene().removeItem(self.m_callouts.pop())

    #adds a point and scales the axis if necessary
    def refresh_stats(self,xdata: float, ydata: float):
        #keep track of the data for cursor
        self.xdata.append(xdata)
        self.ydata.append(ydata)
        #autoscaling
        if ydata > 0.9*self.max:
            self.max = 1.2*ydata
            if self.log:
                self.y_axis.setRange(1,self.max);
            else:
                self.y_axis.setRange(0,self.max)

        #add the data
        self.series.append(xdata,ydata)

    def set_xlim(self,min,max):
        self.x_axis.setRange(min, max)
        self.rangeX = max - min

    #resets the plot
    def cla(self):
        while len(self.m_callouts) != 0:
            self.scene().removeItem(self.m_callouts.pop())
        self.ydata = []
        self.xdata = []
        self.max = 10
        self.series.clear()



#the bar chart for the optimizing
class BarChartView(qtch.QChartView):

    max = 100
    min = 0
    def __init__(self,parent):
        super().__init__()
        self.chart = qtch.QChart()#make a chart
        self.setChart(self.chart)#set this ChartViews chart to the created chart
        self.series = qtch.QBarSeries()#make a bar series for the chart
        self.series.setBarWidth(1)
        self.chart.addSeries(self.series)#add the bar to the chart
        self.chart.legend().setVisible(False)
        self.chart.setContentsMargins(-10, -10, -10, -10)
        self.bar_set = qtch.QBarSet('')
        self.series.append(self.bar_set)

        self.bar_set.append(20)

        self.x_axis = qtch.QBarCategoryAxis()

        self.x_axis.setVisible(False)
        self.chart.setAxisX(self.x_axis)
        self.series.attachAxis(self.x_axis)

        self.y_axis = qtch.QValueAxis()

        self.y_axis.setRange(0,100)
        self.y_axis.setVisible(False)
        self.chart.setAxisY(self.y_axis)
        self.series.attachAxis(self.y_axis)

        self.series.setLabelsVisible(True)
        self.chart.layout().setContentsMargins(0,0,0,0)
        self.chart.setTheme(qtch.QChart.ChartThemeDark)
        self.setMinimumSize(10,50)
        self.setParent(parent)


    def refresh_stats(self,ydata):
        while ydata > self.max:
            self.min = self.max
            self.max *= 10
            self.y_axis.setRange(0,self.max)


        while ydata < self.min:
            self.max /= 10
            if self.min == 100:
                self.min = 0
            else:
                self.min /= 10
            self.y_axis.setRange(0,self.max)

        #rounding if over 1 million to prevent cut off
        if ydata > 1e6:
            digits = len(str(ydata))
            ydata = round(ydata,-(digits - 3))

        self.bar_set.replace(0,ydata)
        self.series.append(self.bar_set)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = View()
    window.refresh_stats(0,0)
    window.refresh_stats(1,1)
    window.refresh_stats(2,2)
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
