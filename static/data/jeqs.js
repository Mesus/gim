$(function() {    
Morris.Area({
        element: 'jeqs',
        data: [{
            period: '2010 Q1',
            iphone: 2666
        }, {
            period: '2010 Q2',
            iphone: 2000
        }, {
            period: '2010 Q3',
            iphone: 4912
        }, {
            period: '2010 Q4',
            iphone: 3767
        }, {
            period: '2011 Q1',
            iphone: 6810
        }, {
            period: '2011 Q2',
            iphone: 5670
        }, {
            period: '2011 Q3',
            iphone: 4820
        }, {
            period: '2011 Q4',
            iphone: 15073
        }, {
            period: '2012 Q1',
            iphone: 10687
        }, {
            period: '2012 Q2',
            iphone: 8432
        }],
        xkey: 'period',
        ykeys: ['iphone'],
        labels: ['iPhone'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });
});
