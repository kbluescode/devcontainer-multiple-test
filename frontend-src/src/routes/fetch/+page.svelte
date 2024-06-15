<script>
  let key = "";
  let value;
  let error;

  async function getVal(_e) {
    error = null;
    const response = await fetch(`http://api.localhost/get/${key}`);
    const resp = await response.json();
    if (resp.error) {
      error = resp.error;
    }
    value = resp.value;
  }
</script>

<input bind:value={key} />
<button on:click={getVal}>Go fetch</button>
<p>Key: {key}</p>
<p>Value: {value}</p>
{#if error}
  <p>Error: {error}</p>
{/if}
