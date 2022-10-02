<template>
    <div>
        Codes:
        <div v-for="row in rows">
            {{row}}
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            rows: [],
            responseLength: 0
        }
    },
    methods: {
        getDataFromStream(_data) {
            return this.axios({
                url: `http://127.0.0.1:5000/stream`,
                method: 'GET',
                onDownloadProgress: progressEvent => {
                    let dataChunk = progressEvent.currentTarget.response;
                    let lines = dataChunk.substring(this.responseLength).split("\n")
                    this.responseLength = dataChunk.length
                    // dataChunk = dataChunk.replaceAll("'", "")
                    for (let line of lines) {
                        this.rows.push(line)
                    }
                }


            }).then(({ data }) => Promise.resolve(data));
        }

    },
    created() {
        this.getDataFromStream();
    }
}

</script>