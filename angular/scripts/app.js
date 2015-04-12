'use strict';

var restApp = angular.module('restApp', [
    'ui.router'
])
.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('snippets', {
            url: '/snippets',
            templateUrl: 'partials/snippets.partial.html',
            controller: 'restAppController',
            data: {
                pageTitle: 'Sample API data'
            }
        });
});
