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
      :card-data="[{'title':'Unique Users', 'value': 25}, {'title':'Total Calls', 'value': 250}, {'title':'Failed Calls', 'value': 2}]"
      ></OverviewCards>
      </vs-col>
    </vs-row>

    <vs-row
      vs-w="11.5"
    >
      <vs-col vs-offset="0.5" vs-type="flex" vs-align="flex-start" vs-w="12">
        <div
          class="chart"
        >
          <app-chart/>
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

    }
  },

};
</script>

<style scoped>

</style>