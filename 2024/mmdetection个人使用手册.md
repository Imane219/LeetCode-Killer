本文将讲述目标检测小白第一次使用mmdetection时应如何做。

## 更换数据集

按照官网，将数据集更换成COCO格式。请注意，不仅是key需要更换，value的含义也要换过来。比如COCO的bbox中数值指的是左上角x,y坐标的值以及w,h的绝对长度；而YOLO格式中则是bbox中心的坐标x_centor/w_image, y_centor/y_image以及w/w_image, h/h_image.

数据集更换后，需要修改config文件。选择一个config文件例如：`configs/cascade_rcnn/cascade-rcnn_r50_fpn_20e_coco.py`，可以发现它引用了四个`_base_`中的设置，mmengine会自动加载这些设置。

![](figures/5.png)

这四个设置分辨是：

- cascade-rcnn，bkb为rn50+fpn的网络结构配置文件，在当前步骤我们无需修改。
- 数据集配置, coco_detection为其默认配置之一，_val是我copy它的自己