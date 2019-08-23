#### 内容回顾

##### BOM

- location.reload() 全局刷新页面

- location.href

- location.hash

- location.pathname

- location.hostname

- location.origin 源(同源策源(查阅资料))始地址

  

##### client,offset,scroll

- document.documentElement.clientWidth 屏幕可视宽度
- offsetTop 到页面顶部的距离
- scrollTop 页面卷起的高度

##### jQuery核心的思想

```javascript
write less, do more 写的少 做的多
```

##### jQuery的入口函数

```javascript
//它们 是没有事件覆盖现象
$(document).ready(fn);
$(fn);

//窗口加载 
$(window).ready(fn)
```

##### 为什么要学习jQuery

js的先天性不足

- window.onload()的事件覆盖现象
- 代码容错量大
- 兼容性不好
- 动画效果难以实现
- 代码比较乱

##### jQuery的98%的都是方法

##### jQuery的选择器(选中DOM)*

$('')

###### 基本选择器

- id选择器
- 类选择器
- 标签选择器
- 子代
- 后代
- 组合
- 交集
- 通配符
- 兄弟 + ~

###### 基本过滤选择器 + 属性选择器

- $('li:eq(index)')
- :gt(index) 
- :lt(index) 
- :odd
- :even
- :first
- :last
- input[type='text']

###### 筛选的方法***

- [x] $('li').eq(index)
- [x] find(selector) 后代
- [x] children() 亲儿子
- [x] parent() 亲爹
- [x] siblings() 选取兄弟(除了它自己 )

###### jQuery和js对象相互转换**

```javascript
//js==>jquery
$(js对象)
jquery对象 => js对象
$('li')[index];
$('li').get(index);
```

##### jQuery的动画

###### 显示隐藏动画

```javascript
show();
hide(3000,fn);
toggle(3000,fn)
```

###### 卷帘门效果

```javascript
slideDown(); //显示
slideUp();//隐藏
slideToggle() //开关式的显示隐藏
```

###### 淡入淡出效果

```javascript
fadeIn();//显示
fadeOut();//隐藏
fadeToggle()//开关式的显示隐藏
```





##### 额外内容

```javascript
click
css(); //样式属性操作  oDiv.style.xxx
text(); //innerText
html(); //innerHtml
val();        //value

addClass();
removeClass()

```



#### 今日内容

##### jQuery的自定义动画

```javascript
$(selector).animate({css的属性},speed,fn)
```

要想修改背景颜色,那么要借助与jquery的插件 https://github.com/jquery/jquery-color/blob/master/jquery.color.js

##### 使用动画的时候一定要先stop() 再开启动画,使用定时器的时候 要先清定时器,再开定时器

##### jQuery的DOM操作

###### 标签属性操作

```javascript
attr()  //getAttrbute() setAttrbute() 路径的相对地址
removeAttr() //removeAttibute()
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="./xiaohua.jpg" alt="" >
<script src="./libs/jquery-3.3.1.js"></script>
<script>
    $(function () {

        //attr
        //获取值
        console.log($('img').attr('src')); //./xiaohua.jpg
        //设置值
        $('img').attr('alt','美女'); //./xiaohua.jpg

         //设置多个标签属性值
         $('img').attr({
             'aaa':'美女',
             'bbbb':'个哈哈哈'
         });

         //移除 removeAttr()
        setTimeout(()=>{
            //移除单个属性
           // $('img').removeAttr('alt');


           //移除多个属性
            $('img').removeAttr('alt aaa bbbb');
        },3000)

    })
</script>
</body>
</html>
```

> 注意: 不要使用attr()或者prop()来设置类名 

###### 对象属性操作

```
prop()  //oDiv.id  
removeProp()  //oDiv.id = ''
```

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            border: 1px solid red;
        }
    </style>
</head>
<body>
<img src="./xiaohua.jpg" alt=""  class="box">
<script src="./libs/jquery-3.3.1.js"></script>
<script>
    $(function () {

        //获取值
        console.log($('img').prop('src'));
        $('img').prop('aaaa','美女');
        $('img').prop({
            'bbb':'哈哈',
            'aa':'嘿嘿'
        });



        //移除 removeProp() 删除一个属性
        $('img').removeProp('aa');
        $('img').removeProp('bbb');

        console.log($('img'));


        setTimeout(()=>{

        },3000)

    })
</script>
</body>
</html>
```

###### 类的操作

```javascript
addClass() //添加类
removeClass() //移除
toggleClass() //添加|移除
```



###### 值的操作

```javascript
//如果不传参数 表示获取值
//如果传参数,表示设置值
text();// innerText 设置文本的内容
html(); //innerHTML 即设置文本又设置标签
val(); //value
```



###### 样式属性操作

```javascript
//如果有一个参数,参数是字符串表示获取值,参数是对象,表示设置多个值
//如果有两个参数,表示设置值
$(selector).css();
```

###### 操作input中value的值

下拉列表

```html

<select name="timespan" id="timespan" class="Wdate"  multiple="multiple" >
    <option value ='1' selected>alex</option>
    <option value = '2' selected="">wusir</option>
    <option value = '3'>wulaoban</option>
</select>
```

```java
总结:
1.如果option中的属性有value,优先使用value设置
$('#timespan').val(['1','3']);//选中1 和3选项
2.如果没有value,那么使用标签的文本内容设置
$('#timespan').val(['alex','wulaobnan']) //选中1 和 3 选项

```



##### 今日作业

- 百度导航栏样式搭建
- 天气状况显示隐藏(css())
- 换肤显示隐藏(slideDown|slideUp)
- 用户名显示隐藏(addClass()|removeClass())
- 更多产品淡入淡出显示隐藏(fadeIn()|fadeOut())

##### 预习内容

https://www.cnblogs.com/majj/p/9119467.html  文档的操作

