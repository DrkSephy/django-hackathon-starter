angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SessionsCtrl', function($scope, Session) {
    $scope.sessions = Session.query();
})

