<template>
  <div>

    <vs-row
      vs-w="12"
      style="margin-bottom: 10px"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="center" vs-justify="center" vs-w="12">
        <h2>DASHBOARD</h2>
      </vs-col>
    </vs-row>
    <div
      style="margin-bottom: 50px;"
    ></div>
    <vs-row
      vs-w="12"
      style="margin-bottom: 10px"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="7">
        OVERVIEW
      </vs-col>
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-end" vs-justify="flex-end" vs-w="3.6">
        <period-filter
          @update-time-filter="handleFilterChange"
        />
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
    <div
      style="margin-bottom: 50px;"
    ></div>
    <vs-row
      vs-w="12"
      style="margin-bottom: 25px"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
        USAGE
      </vs-col>
    </vs-row>
    <vs-row
      vs-w="11.5"
      style="margin-bottom: 25px"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
        <vs-card>
          <app-table
            v-if="Object.keys(table).length > 0"
            :table="table"
          />
        </vs-card>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
  import OverviewCards from '@/components/OverviewCards';
  import AppChart from '@/components/AppChart';
  import PeriodFilter from '@/components/PeriodFilter';
  import AppTable from '@/components/AppTable';

  export default {
    name: 'AnalyticsDashboard',
    components: { AppTable, PeriodFilter, AppChart, OverviewCards },
    data () {
      return {
        tiles: [],
        chart: {},
        table: {}
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
          this.table = response['table'];
        }).catch(error => {
          console.log(error);
        });
      }
    }
  };
</script>

<style scoped>

</style>