angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SessionsCtrl', function($scope, Session) {
    $scope.sessions = Session.query();
    console.log($scope.sessions);
})

.controller('SessionCtrl', function($scope, $stateParams, Session) {
    $scope.session = Session.get({sessionId: $stateParams.sessionId});
});


/* 

.controller('SessionsCtrl', function($scope, Session) {
    $scope.sessions = Session.get();
    console.log($scope.sessions);
})

*/