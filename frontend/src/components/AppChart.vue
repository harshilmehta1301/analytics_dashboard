<template>
  <vs-row
      vs-w="12"
      vs-type="flex"
    >
         <VueEcharts
           id="analysis-chart"
           ref="chart"
           :style=graphSize
           :option="chartOptions"
        />

  </vs-row>
</template>

<script>
  import { VueEcharts } from "vue3-echarts";
  export default {
    name: 'AppChart',
    components: {VueEcharts},
    // props:{
    //   width:Number
    // },
    data() {
      return {
        'graphSize': {
          'width': null,
          'height': null,
        },
        chartOptions:{
  title: {
    text: 'Traffic Sources',
    left: 'center',
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)',
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    data: ['Direct', 'Email', 'Ad Networks', 'Video Ads', 'Search Engines'],
  },
  series: [
    {
      name: 'Traffic Sources',
      type: 'pie',
      radius: '55%',
      center: ['50%', '60%'],
      data: [
        { value: 335, name: 'Direct' },
        { value: 310, name: 'Email' },
        { value: 234, name: 'Ad Networks' },
        { value: 135, name: 'Video Ads' },
        { value: 1548, name: 'Search Engines' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)',
        },
      },
    },
  ],
}
      }
    },
    mounted(){
       this.updateGraphSize();
    },
    methods:{
      updateGraphSize: function () {
        this.$nextTick(() => {
        console.log(window.innerWidth)
        const width = window.innerWidth;
        let height;
        if (width > 800) {
          height = width * 0.3;
        }
        else if (width > 500) {
          height = width * 0.4;
        } else {
          height = width * 0.6;
        }
        this.graphSize = {
          'width': `${ width - 95 }px`,
          'height': `${ height }px`,
        };
      });
      }
    }
  };

</script>

<style scoped>

</style>