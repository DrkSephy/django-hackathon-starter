'use strict';

restApp.factory('githubTopContributionsFactory', function($http) {
    return {
        get: function() {
            return $http({
                url: 'http://127.0.0.1:8000/hackathon/githubTopRepositories/',
                method: 'GET',
            });
        }
    };
});
