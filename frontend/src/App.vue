<template>
  <AnalyticsDashboard></AnalyticsDashboard>
  <!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
</template>

<script>
  import AnalyticsDashboard from '@/components/AnalyticsDashboard';

  export default {
    name: 'App',
    components: {
      AnalyticsDashboard
    }
  };
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 15px;
  }


  ::-webkit-scrollbar {
    width: 6px;
  }


  ::-webkit-scrollbar-track {
    background-color: #f1f1f1;
  }


  ::-webkit-scrollbar-thumb {
    background-color: #BEBEBE;
    border-radius: 3px;
  }


  ::-webkit-scrollbar-thumb:hover {
    background-color: #555;
  }

</style>
