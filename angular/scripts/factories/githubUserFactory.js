'use strict';

restApp.factory('githubUser', function($http) {
    return {
        get: function() {
            return $http({
                url: 'http://127.0.0.1:8000/hackathon/githubUser/',
                method: 'GET',
            });
        }
    };
});
