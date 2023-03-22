<script lang="ts">
	import type { Questions } from '../types';
	export let questions: Questions;
</script>

{#if questions}
	<div>
		<h2>Technical Questions</h2>
		{#each questions.tech as q}
			<div class="block">
				<p class="question">
					{q.question}
				</p>
			</div>
			<br />
		{/each}
		<h2>Behavior Questions</h2>
		{#each questions.behavior as q}
			<div class="block">
				<p class="question">
					{q.question}
				</p>
			</div>
			<br />
		{/each}
	</div>
{/if}

<style>
	.block {
		border-bottom: 0.5px solid lightgrey;
		margin: 8px 8px 20px 8px;
		padding: 16px 16px 16px 0px;
	}
	.question {
		font-size: 18px;
	}
</style>
