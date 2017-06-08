var SecureMail = angular.module('securemail', ['ngRoute', 'ngResource'])

  .factory('SecureMail', function($resource) {
    var SecureMail = $resource(':protocol//:server/:a/:b', {
      protocol: 'http:',
      server: '86.45.70.108:8080'
    });
    return SecureMail;
  })


  .config(function($routeProvider) {
    $routeProvider
      .when('/', {
        controller: 'LoginCtrl',
        templateUrl: 'login.html'
      })
      .when('/inbox', {
        controller: 'InboxCtrl',
        templateUrl: 'inbox.html'
      })
      .otherwise({
        redirectTo: '/'
      });
  })

  .config(['$locationProvider', function($locationProvider) {
    $locationProvider.hashPrefix('');
  }])

  .controller('LoginCtrl', function($scope, $location, SecureMail, Inbox) {
    $scope.Inbox = Inbox;

    $scope.Register = function() {
      var results = SecureMail.get({
        a: 'register'
      });
      $scope.Inbox.setInboxDetails(results);
      GotoInbox();
    };

    $scope.Login = function() {
      $scope.Inbox.setInboxDetails($scope.Inbox);
      GotoInbox();
    };

    GotoInbox = function() {
      $location.path('/inbox');
    };
  })

  .controller('InboxCtrl', function($scope, SecureMail, Inbox) {
    $scope.Inbox = Inbox;
  });

SecureMail.factory('Inbox', function() {
  var totp = new jsOTP.totp();
  var inboxDetails = {
    ID: '',
    Secret: ''
  };
  var messages = [];
  return {
    getID: function() {
      return inboxDetails.ID;
    },
    getToken: function() {
      return (inboxDetails.Secret && inboxDetails.Secret.length == 16 ? totp.getOtp(inboxDetails.Secret) : '');
    },
    setInboxDetails: function(i) {
      inboxDetails = i;
    },
    addMessages: function(i) {
      if (i.status == 200) {
        messages.push(i);
      }
    },
    getMessages: function() {
      return messages;
    }
  };
});
