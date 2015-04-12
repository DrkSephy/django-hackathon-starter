angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SnippetsCtrl', function($scope, Snippets) {
    $scope.snippets = Snippets.query();
})

.controller('githubUserCtrl', function($scope, githubUser) {
    $scope.sessions = githubUser.get();
    console.log($scope.sessions);
})

