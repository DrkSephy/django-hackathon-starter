'use strict';

restApp.controller('appController', function($scope, $location) {
    $scope.siteTitle = 'REST App';

    $scope.$on('$stateChangeSuccess', function(event, toState) {
        $scope.pageTitle = toState.data.pageTitle;
    });

    $scope.isActive = function(viewLocation) {
        return viewLocation === $location.path();
    };
});
