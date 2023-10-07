<template>
      <vs-card>
        <template v-slot:header>
          <h3>
            {{ header }}
          </h3>
        </template>
        <template v-slot>
            <span
            style="font-size: 20px; color:blue;"
            >
              {{ content }}
            </span>
        </template>
      </vs-card>
</template>

<script>
  export default {
    name: 'AppCard',
    props: {
      header: {
        type: String,
        default: '',
      },
      content: {
        type: Number,
        default: 0,
      },
    }
  };
</script>

<style scoped>

</style>