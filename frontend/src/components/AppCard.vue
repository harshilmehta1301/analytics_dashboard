<template>
  <vs-card class="custom-card">
    <template v-slot:header>
      <h3>
        {{ header }}
      </h3>
    </template>
    <div
      class="center-content"
    >
            <span
              style="font-size: 20px; color:blue;"
            >
              {{ content }}
            </span>
    </div>
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
  .custom-card {
    width: 170px; /* Set your desired width */
    height: 100px; /* Set your desired height */
  }

  .center-content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    margin-top: 10px;
  }
</style>