<template>
  <div>
    <main>
      <form @submit.prevent="submit">
        <div class="form-group d-flex flex-row p-2"
          v-for="(btype, bname) in picodes.sets[setname].buttons[currentButtonIndex]" :key="picodes.sets[setname].buttons[currentButtonIndex].id">
          <label class="p-2" for="pwd">{{ bname }}:</label>
          <input class="p-2" type="input" v-model="picodes.sets[setname].buttons[currentButtonIndex][bname]" />
          <div class="btn-group" role="group">
            <button class="btn btn-sm btn-secondary" @click="openLearnDialog">Learn...</button>
            <button class="btn btn-sm btn-secondary">Schedule...</button>
          </div>
        </div>
        <button class="btn btn-primary" type="submit">
          Save
        </button>
      </form>
    </main>

    
  </div>
</template>

<script>
export default {
  props: ['picodes', 'setname', 'currentButtonIndex'],
  methods: {
    openLearnDialog(bname) {
      this.currentButtonName = bname
      debugger
      reveal()
    }
  },
  data() {
    return {
      currentButtonName: ""
    }
  }
};

import LearnCodeDialog from './LearnCode.vue'
import { createConfirmDialog } from 'vuejs-confirm-dialog'

const { reveal, onConfirm, onCancel } = createConfirmDialog(LearnCodeDialog)


onConfirm((e) => {
  console.log(`Confirmed! ${JSON.stringify(e)}`)
  e.me.$parent.$parent.$emit('newcode', {code: e.code.code, bname: this.currentButtonName});
})
onCancel(() => {
  console.log('Canceled!')
})
</script>

