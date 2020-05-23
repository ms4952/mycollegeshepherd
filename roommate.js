$(document).ready(function () {

    let geoOptions = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };

    function updateBudgetOnRangeChange() {
        $("#minBudget").val($("#minBudgetRange").val());
        $("#maxBudget").val($("#maxBudgetRange").val());
    }

    function updateBudgetOnInputChange() {
        $("#minBudgetRange").val($("#minBudget").val());
        $("#maxBudgetRange").val($("#maxBudget").val());
    }

    $("#locateMe").on("click", function (event) {
        $("#locateMe").addClass("locating");
        navigator.geolocation.getCurrentPosition(function () {
            debugger;
            $("#locateMe").removeClass("locating");
        }, function(err){
            console.error(err);
            $("#locateMe").removeClass("locating");
        }, geoOptions);
    });

    $("#budget input[type=range]").on("input change", updateBudgetOnRangeChange);
    $("#budget input[type=number]").on("input change", updateBudgetOnInputChange);
    updateBudgetOnRangeChange();
});