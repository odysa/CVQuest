<script lang="ts">
	import { FileDropzone, Button, Headline, Subhead } from 'attractions';
	import FoldableListItem from '../components/foldlist.svelte';
	import type { Status, Questions } from '../types';
	let status: Status = 'Init';
	let file: File;
	let questions: Questions;

	function handleFileInput(files: File[]) {
		if (files.length > 1) {
			// very unlikely to happen
			alert('must upload only one file');
			return;
		}
		file = files[0];
	}

	async function generateQuestions() {
		// Add your logic to generate questions and answers
		// based on the selected file

		// For demonstration purposes, we'll add a sample question and answer
		questions = {
			tech: [
				{ question: 'What is the purpose of Svelte?', answer: '' },
				{ question: 'What is the purpose of Svelte?', answer: '' },
				{ question: 'What is the purpose of Svelte?', answer: '' }
			],
			behavior: [
				{ question: 'What is the purpose of Svelte?', answer: '' },
				{ question: 'What is the purpose of Svelte?', answer: '' },
				{ question: 'What is the purpose of Svelte?', answer: '' }
			]
		};
	}
</script>

<div id="main-content">
	<Headline>CVQuest -- Personal interview questions from your resume</Headline>
	<Subhead>
		<a href="https://github.com/odysa/CVQuest">CVQuest</a> is an open-source project. Feel free to
		run locally or deploy your own. <br /> We will <b>NOT</b> store your personal data.
		<a href="https://github.com/odysa/CVQuest">
			<img
				src="https://img.shields.io/github/stars/odysa/CVQuest.svg?style=social&label=Star&maxAge=259200"
				alt=""
			/>
		</a>
		<a href="https://github.com/odysa">
			<img
				src="https://img.shields.io/github/followers/odysa.svg?style=social&label=Follow&maxAge=259200"
				alt=""
			/>
		</a>
	</Subhead>
	<FileDropzone accept=".pdf" max={1} />
	<Button id="generate-button" filled round on:click={generateQuestions}
		><div id="generate-button-text">Generate 🎲</div></Button
	>

	<FoldableListItem {questions} />
</div>

<style>
	#main-content {
		max-width: 900px; /* adjust the width as needed */
		margin: 0 auto;
		display: flex;
		flex-direction: column;
	}
	#generate-button-text {
		margin: 0 auto;
	}
</style>
