<template>
  <app-modal
  v-if="showFilter"
  >
  <div class="time-filter">
    <form>
      <div class="form-group">
        <label>Select Time Range:</label>
        <select
          class="custom-select"
          v-model="timeRange"
          style="margin-top: 20px; "
        >
          <option value="24_hours">Last 24 hours</option>
          <option value="7_days">Last 7 days</option>
          <option value="custom">Custom time range</option>
        </select>
      </div>
      <div class="form-group" style="margin-top: 30px;" v-if="timeRange === 'custom'">
        <label for="start-date">Start Date:</label>
        <br>
        <input
          type="datetime-local"
          class="form-control"
          v-model="customStartDate"
          id="start-date"
          style="margin-bottom: 30px;"
        >
        <br>
        <label for="end-date">End Date:</label>
        <br>
        <input
          type="datetime-local"
          class="form-control"
          v-model="customEndDate"
          id="end-date"
        >
      </div>
      <div class="form-group">
        <vs-row
          vs-type="flex"
          vs-w="12"
          vs-justify="flex-end"
          style="margin-top: 30px;"
        >
          <vs-button
           style="margin-right: 10px; width: 70px;"
           color="#26619c"
           @click="handleTimeRangeChange"
          >
            Apply
          </vs-button>
          <vs-button
            style="width: 70px;"
            type="border"
            color="grey"
            @click="closeModal"
          >
            Cancel
          </vs-button>
        </vs-row>

      </div>
    </form>

  </div>
  </app-modal>
  <vs-row
      vs-w="12"
      style="margin-bottom: 25px"
    >
     <vs-col vs-type="flex" vs-align="flex-end" vs-justify="end" vs-w="11.5">
        <div class="selected-time-range" >
              <vs-chip v-if="selectedTimeRange === '24_hours'">
               <button
                 class="chip-button"
                 @click="openModal">
                  Last 24 hours
               </button>
              </vs-chip>
              <vs-chip v-else-if="selectedTimeRange === '7_days'">
                <button
                  class="chip-button"
                  @click="openModal">
                  Last 7 Days
               </button>
              </vs-chip>
              <vs-chip v-else-if="selectedTimeRange === 'custom'">
                <button
                  class="chip-button"
                  @click="openModal">
                  {{ customStartDate }} to {{ customEndDate }}
               </button>
              </vs-chip>
        </div>
     </vs-col>
  </vs-row>
</template>

<script>
import AppModal from '@/components/AppModal';
export default {
  name: 'PeriodFilter',
  components: { AppModal },
  data() {
    return {
      selectedTimeRange: '24_hours',
      timeRange: '24_hours',
      customStartDate: '',
      customEndDate: '',
      showFilter:false
    };
  },
  methods: {
    handleTimeRangeChange() {
      if (this.selectedTimeRange !== this.timeRange) {
        const payload ={
          'time_period': this.timeRange
        }
        if (this.timeRange === 'custom'){
          payload['start_range'] = this.customStartDate;
          payload['end_range'] = this.customEndDate;
        }
        this.$emit('update-time-filter', payload);
        this.selectedTimeRange = this.timeRange;
        this.closeModal();
      }
    },
    openModal(){
      this.showFilter = true;
    },
    closeModal(){
      this.showFilter = false;
    }
  }
};
</script>

<style scoped>
/* Custom CSS for styling */
.time-filter {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  z-index: 9999;
}

.time-filter-title {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

.custom-select {
  width: 70%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 20px;
  height: 40px;
}

.form-control {
  width: 70%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 20px;
  height: 40px;
  margin-top: 20px;
  background: #EFEFEF;
}

.selected-time-range {
  margin-top: 15px;
  font-weight: bold;
}

.chip-button{
  border: none;
  background: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
  color: inherit;
  font: inherit;
  text-align: inherit;
  text-decoration: none;
}

.close {
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}
</style>
