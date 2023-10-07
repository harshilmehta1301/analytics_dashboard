<template>
  <vs-row
      vs-w="12"
      vs-type="flex"
    >
         <VueEcharts
           id="analysis-chart"
           ref="chart"
           :style="{'width': `${graphSize['width']}`, 'height': `${graphSize['height']}`}"
           :option="chart"
        />

  </vs-row>
</template>

<script>
  import { VueEcharts } from "vue3-echarts";
  export default {
    name: 'AppChart',
    components: {VueEcharts},
    props:{
      chart:Object
    },
    data() {
      return {
        'graphSize': {
          'width': null,
          'height': null,
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