<template>
    <div>Settings:</div>
    <div>GPIO PIN: {{ picodes.gpio }}</div>
    <div>Set: {{ setname }}</div>
    <div>Protocol: {{ picodes.sets[setname].protocol }}</div>
    <div>PulseLength: {{ picodes.sets[setname].pulselength }}</div>
</template>


<script>
export default {
    props: ['picodes', 'setname'],
};
</script>