Object.size = function(obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};


$(".search-input").on('keyup', () => {
    $('#search-inf').addClass('hide')
    let val = $(".search-input").val()
    $.ajax({
        url : "/search/", // the endpoint
        type : "POST", // http method
        data : { 'query' : val }, // data sent with the post request
        dataType: "json",

        // handle a successful response
        success : (resp) => {
            $('#search-counter').removeClass('hide')
            $('#search-counter').empty()
            $('.search-results').empty()
            $("#search-counter").append(`<span class="counter-results">${Object.size(resp)}</span>
                            Results for your search
            `)
            for (var key in resp){
                let title = resp[key]['title']
                let date = resp[key]['date']
                $('.search-results').append(`
                    <a href="${"http://"+window.location.hostname+":5000/blog/post/"+key}">
                        <h4>${title}<span class="search-date">Published — ${date}</span></h4>
                    </a>
                `)
            }
        },

        // handle a non-successful response
        error : (xhr,errmsg,err) => {
            $('#search-counter').removeClass('hide')
            $('#search-counter').empty()
            $("#search-counter").append(`
                <span class="counter-results">0</span>
                            Results for your search
            `)
            
        }
    });
})


$('.subscribe-click').on('click', () => {
    $('.ityped-sub').css({
        'display':'block'
    })
    $('.ityped-wrap').css({
        'display':'none'
    })
    $.ajax({
        url : "/newsletter/", // the endpoint
        type : "POST", // http method
        data : { 'email' :$('.subscribe-email').val() }, // data sent with the post request

        // handle a successful response
        success : (resp) => {
            var newsletter = ["Thanks for subscribing"]
            var subscribe = $("#subscribe");
            if (subscribe) {
                let typed = ityped.init(document.querySelector(".ityped-sub"), {
                    strings: newsletter,
                    showCursor: true,
                    typeSpeed: 150,
                    startDelay: 500,
                    backDelay: 5000,
                });
            }
            
        },

        // handle a non-successful response
        error : (xhr,errmsg,err) => {
            var newsletter = ["Oops, an error occured"]
            var subscribe = $("#subscribe");
            if (subscribe) {
                let typed = ityped.init(document.querySelector(".ityped-sub"), {
                    strings: newsletter,
                    showCursor: true,
                    typeSpeed: 150,
                    startDelay: 500,
                    backDelay: 5000,
                });
            }
            
        }
    });
    setTimeout(() => {
        $('.ityped-sub').css({
            'display':'none'
        })
        $('.ityped-wrap').css({
            'display':'block'
        })
        location.reload()
    }, 5000)

})