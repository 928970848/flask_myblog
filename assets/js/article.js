$(function(){
    var converter = new showdown.Converter({
        tables:true,
        tableCellSplitter: '|',
    });
    var article_html = converter.makeHtml($('#article_content').val())
    $('#article_viewer').html(article_html)
})