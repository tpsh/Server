$(document).ready(function() {

    // page is now ready, initialize the calendar...

    $('#calendar').fullCalendar({
        lang : "ru",
        header : {
            left: "",
            center: "title",
            right: ""
        }
    });

    $('#calendar_day').fullCalendar({
            defaultView : 'basicWeek' ,
            lang : "ru",
            contentHeight: 150,
            header: "false"
        // put your options and callbacks here
    });

    $('.fc-day-number').append('<div></div>');

    var date = new Date ;
    monthA = 'января,февраля,марта,апреля,мая,июня,июля,августа,сентября,октября,ноября,декабря'.split(',');
    document.getElementById("my_date").innerHTML = ('0' + date.getDate()).slice(-2) + ' ' + (monthA[date.getMonth() + 1])  + ' ' + date.getFullYear()
;

}); 

