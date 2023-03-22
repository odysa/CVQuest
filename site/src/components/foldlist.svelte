<script lang="ts">
	import type { Questions } from '../types';
	export let questions: Questions;
</script>

{#if questions}
	<div>
		<h2>Technical Questions</h2>
		{#each questions.technical_questions as q}
			<div class="block">
				<p class="question">
					{q}
				</p>
			</div>
		{/each}
		<h2>Behavior Questions</h2>
		{#each questions.behavior_questions as q}
			<div class="block">
				<p class="question">
					{q}
				</p>
			</div>
		{/each}
	</div>
{/if}

<style>
	.block {
		border-bottom: 0.5px solid lightgrey;
		margin: 8px 8px 8px 8px;
		padding: 14px 14px 14px 0px;
	}
	.question {
		font-size: 18px;
	}
</style>
