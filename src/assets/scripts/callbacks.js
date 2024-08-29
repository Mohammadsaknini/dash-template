window.dash_clientside = Object.assign({}, window.dash_clientside, {
    svm_page: {
        disable_slider_param_degree: function (kernel) {
            return kernel !== "poly"
        },
    }
});