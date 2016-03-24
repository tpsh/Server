$(document).ready(function() {

    // page is now ready, initialize the calendar...
    $('#calendar').fullCalendar({
        lang : "ru",
        // put your options and callbacks here
        dayClick: function(date, jsEvent, view) {

        alert('Clicked on: ' + date.format());

        alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);

        alert('Current view: ' + view.name);

        // change the day's background color just for fun
        $(this).css('background-color', 'red');


        }
    
    });

    $('#calendar_day').fullCalendar({
            defaultView : 'basicWeek' ,
            lang : "ru",
            contentHeight: 150
        // put your options and callbacks here
    });



    $('.fc-day-number').append('<div>Test</div>');

}); 