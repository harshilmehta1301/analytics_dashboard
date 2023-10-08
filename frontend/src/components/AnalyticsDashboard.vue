<template>
  <div>
    <vs-row>
      <period-filter
        @update-time-filter="handleFilterChange"
      />
    </vs-row>
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
        />
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
          <vs-card>
            <app-chart
              :chart="chart"
            />
          </vs-card>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
  import OverviewCards from '@/components/OverviewCards';
  import AppChart from '@/components/AppChart';
  import PeriodFilter from '@/components/PeriodFilter';

  export default {
    name: 'AnalyticsDashboard',
    components: { PeriodFilter, AppChart, OverviewCards },
    data () {
      return {
        tiles: [],
        chart: {}
      };
    },
    beforeMount: function () {
      this.getAnalytics();
    },
    methods: {
      handleFilterChange: function (payload) {
        this.getAnalytics(payload);
      },
      getAnalytics: function (payload) {
        if (! payload) {
          payload = {};
          payload['time_period'] = '24_hours';
        }
        this.axiosPromise({
          url: '/dashboard/',
          method: 'GET',
          queryParams: payload
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