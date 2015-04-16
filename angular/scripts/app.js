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
                pageTitle: 'Sample API Data'
            }
        })

        .state('githubUser', {
            url: '/githubUser',
            templateUrl: 'partials/githubUser.partial.html',
            controller: 'githubUserController',
            data: {
                pageTitle: 'Github User Data'
            }
        })

        .state('steamSales', {
            url: '/steamSales',
            templateUrl: 'partials/steamSales.partial.html',
            controller: 'steamSalesController',
            data: {
                pageTitle: 'Latest Steam Sales'
            }
        })

        .state('githubTopContributions', {
            url: '/githubTopContributions',
            templateUrl: 'partials/githubTopContributions.partial.html',
            controller: 'githubTopContributionsController',
            data: {
                pageTitle: 'Top Contributions on Github'
            }
        });
});
