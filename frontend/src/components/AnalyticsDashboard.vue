<template>
  <div
  ref="parentElement"
  >
    <vs-row
      vs-w="12"
      style="margin-bottom: 25px"
    >
       <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
          OVERVIEW
       </vs-col>
    </vs-row>
    <vs-row
      vs-w="11.5"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
      <OverviewCards
      :card-data="tiles"
      ></OverviewCards>
      </vs-col>
    </vs-row>

    <div
    style="margin-bottom: 50px;"
    ></div>
    <vs-row
      vs-w="12"
      style="margin-bottom: 25px"
    >
       <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
          ACTIVITIES
       </vs-col>
    </vs-row>
    <vs-row
      vs-w="11.5"
      style="margin-bottom: 20px;"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
        <div
          class="chart"
        >
          <app-chart
          :chart="chart"
          />
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import OverviewCards from '@/components/OverviewCards';
import AppChart from '@/components/AppChart';
export default {
  name: "AnalyticsDashboard",
  components: { AppChart, OverviewCards },
  data () {
    return {
      tiles:[],
      chart:{}
    }
  },
  beforeMount: function () {
    this.getAnalytics();
  },
  methods:{
    getAnalytics: function (){
      this.axiosPromise({
        url: '/dashboard/',
        method: 'GET',
        queryParams:{'time_period':'4_hours'}
        }).then(response => {
          this.tiles = response['tile'];
          this.chart = response['chart'];
        }).catch(error => {
          console.log(error);
        });
      }
    }
};
</script>

<style scoped>

</style>