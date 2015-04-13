// 'starter.controllers' is found in controllers.js
angular.module('starter', ['ionic', 'starter.controllers'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

  .state('app', {
    url: "/app",
    abstract: true,
    templateUrl: "templates/menu.html",
    controller: 'AppCtrl'
  })

  
  .state('app.snippets', {
    url: "/snippets",
    views: {
        'menuContent': {
            templateUrl: "templates/snippets.html",
            controller: 'SnippetsCtrl'
        }
    }
  })

  .state('app.githubUser', {
    url: "/githubUser",
    views: {
        'menuContent': {
            templateUrl: "templates/githubUser.html",
            controller: 'githubUserCtrl'
        }
    }
  })

  .state('app.instagramUser',{
    url: "/instagramUser",
    views: {
      'menuContent': {
        templateUrl: 'templates/instagramUser.html',
        controller: 'instagramUserCtrl'
      }
    }
  })

  .state('app.steamSales', {
    url: '/steamSales',
    views: {
      'menuContent': {
        templateUrl: 'templates/steamSales.html',
        controller: 'steamSalesCtrl'
      }
    }
  });
  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/snippets');
});
