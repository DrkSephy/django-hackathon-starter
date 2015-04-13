'use strict';

restApp.factory('steamSalesFactory', function($http) {
    return {
        get: function() {
            return $http({
                url: 'http://127.0.0.1:8000/hackathon/steamDiscountedGames/',
                method: 'GET',
            });
        }
    };
});
