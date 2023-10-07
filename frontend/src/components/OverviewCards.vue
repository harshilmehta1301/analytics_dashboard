<template>
  <vs-card>
    <template v-slot>
      <vs-row
        vs-type="flex"
        vs-align="center"
        vs-justify="space-around"
        style="padding-top: 20px;"
    >
    <div
      v-for="card in cardData"
      :key="card['title']"
    >
        <app-card
        :header="card['title']"
        :content="card['value']"
        ></app-card>
    </div>

    </vs-row>
    </template>
  </vs-card>

</template>

<script>
  import AppCard from '@/components/AppCard';
  export default {
    name: 'OverviewCards',
    components: { AppCard },
    props: {
      cardData: {
        type: Array,
        default: () => [],
      },
    }
  };
</script>

<style scoped>

</style>