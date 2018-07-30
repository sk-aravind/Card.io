angular.module('app.routes', ['ionicUIRouter'])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    

      .state('tabsController.daily1', {
    url: '/daily1',
    views: {
      'tab6': {
        templateUrl: 'templates/daily1.html',
        controller: 'daily1Ctrl'
      }
    }
  })

  .state('tabsController.daily2', {
    url: '/daily2',
    views: {
      'tab6': {
        templateUrl: 'templates/daily2.html',
        controller: 'daily2Ctrl'
      }
    }
  })

  .state('tabsController.daily3', {
    url: '/daily3',
    views: {
      'tab6': {
        templateUrl: 'templates/daily3.html',
        controller: 'daily3Ctrl'
      }
    }
  })

  .state('tabsController.daily4', {
    url: '/daily4',
    views: {
      'tab6': {
        templateUrl: 'templates/daily4.html',
        controller: 'daily4Ctrl'
      }
    }
  })

  .state('tabsController.dailyReward', {
    url: '/daily_reward',
    views: {
      'tab6': {
        templateUrl: 'templates/dailyReward.html',
        controller: 'dailyRewardCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/page1',
    templateUrl: 'templates/tabsController.html',
    abstract:true
  })

  .state('tabsController.home', {
    url: '/home',
    views: {
      'tab3': {
        templateUrl: 'templates/home.html',
        controller: 'homeCtrl'
      }
    }
  })

  .state('homeBad', {
    url: '/home-bad',
    templateUrl: 'templates/homeBad.html',
    controller: 'homeBadCtrl'
  })

  /* 
    The IonicUIRouter.js UI-Router Modification is being used for this route.
    To navigate to this route, do NOT use a URL. Instead use one of the following:
      1) Using the ui-sref HTML attribute:
        ui-sref='tabsController.rewards'
      2) Using $state.go programatically:
        $state.go('tabsController.rewards');
    This allows your app to figure out which Tab to open this page in on the fly.
    If you're setting a Tabs default page or modifying the .otherwise for your app and
    must use a URL, use one of the following:
      /page1/tab3/rewards
      /page1/tab5/rewards
  */
  .state('tabsController.rewards', {
    url: '/rewards',
    views: {
      'tab3': {
        templateUrl: 'templates/rewards.html',
        controller: 'rewardsCtrl'
      },
      'tab5': {
        templateUrl: 'templates/rewards.html',
        controller: 'rewardsCtrl'
      }
    }
  })

  .state('tabsController.habits', {
    url: '/habits',
    views: {
      'tab4': {
        templateUrl: 'templates/habits.html',
        controller: 'habitsCtrl'
      }
    }
  })

$urlRouterProvider.otherwise('/page1/daily1')


});