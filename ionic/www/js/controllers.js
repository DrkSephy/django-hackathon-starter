angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SessionsCtrl', function($scope, Session) {
    $scope.sessions = Session.query();
    console.log($scope.sessions);
})

.controller('githubUserCtrl', function($scope, githubUser) {
    $scope.sessions = githubUser.get();
    console.log($scope.sessions);
})

