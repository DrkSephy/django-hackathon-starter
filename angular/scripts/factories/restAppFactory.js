'use strict';

restApp.factory('restAppFactory', function($http) {
    return {
        get: function() {
            return $http({
                url: 'http://127.0.0.1:8000/hackathon/snippets/',
                method: 'GET',
            });
        }
    };
});
