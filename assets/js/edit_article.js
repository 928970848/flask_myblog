$(function(){

    $("#article_preview_btn").click(function(){
    var converter = new showdown.Converter({
        tables:true,
        tableCellSplitter: '|',
    });
    var article_html = converter.makeHtml($('#content').val())
    $('#article_preview').html(article_html)
    })
})

// 获取两个滚动容器
  var container1 = document.getElementById('content');
  var container2 = document.getElementById('article_preview');

  // 监听第一个容器的滚动事件
  container1.addEventListener('scroll', function() {

  var local_position = container1.scrollTop / container1.scrollHeight
  var local_position2 = parseInt(container2.scrollHeight * local_position)

    // 同步滚动第二个容器
    container2.scrollTop = local_position2;
  });

  // 监听第二个容器的滚动事件
//  container2.addEventListener('scroll', function() {
//    var local_position3 = container2.scrollTop / container2.scrollHeight
//    var local_position4 = parseInt(container1.scrollHeight * local_position3)
//
//    // 同步滚动第一个容器
//    container1.scrollTop = local_position4;
//  });
