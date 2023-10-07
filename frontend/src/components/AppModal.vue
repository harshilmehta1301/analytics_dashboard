<template>
  <div class="modal-container z-level-5">
    <transition
      mode="out-in"
      enter-active-class="animated zoomIn animate--0-25"
      leave-active-class="animated zoomOut animate--0-25"
    >
      <div
        v-if="display"
        :style="customStyle"
        class="modal-content"
      >
        <slot />
      </div>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'AppModal',
    props: {
      customStyle: {
        type: Object,
        default: () => {}
      }
    },
    data: function () {
      return {
        display: false,
      };
    },
    beforeMount () {
      this.$nextTick(() => {
        this.display = true;
      });
    },
  };
</script>

<style scoped>
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 5s ease;
  }
  .modal-content {
    background-color: white;
    border-radius: 8px;
  }
</style>
