<script lang="ts">
	import { FileDropzone, Button, Headline, Subhead } from 'attractions';
	import FoldableListItem from '../components/foldlist.svelte';
	import type { Status, Questions } from '../types';
	let status: Status = 'Init';
	let file: File;
	let questions: Questions;
	type FileChangeEvent = CustomEvent<{ files: File[]; nativeEvent?: Event }>;

	function handleFileInput(e: FileChangeEvent) {
		let files = e.detail.files;
		if (files == null) {
			return;
		}
		if (files.length > 1) {
			// very unlikely to happen
			alert('must upload only one file');
			return;
		}
		if (files[0].size > 1024 * 1024 * 20) {
			alert('file too big');
			return;
		}
		file = files[0];
	}

	async function generateQuestions() {
		if (file == null) {
			alert('file not found');
			return;
		}
		try {
			status = 'Loading';
			const formData = new FormData();
			formData.append('size', file.size.toString());
			formData.append('file', file);
			formData.append('name', file.name);
			formData.append('mimeType', file.type);
			const resp = await fetch('http://localhost:8080/questions/', {
				method: 'POST',
				body: formData
			});
			const json = await resp.json();
			questions = json;
			status = 'Done';
		} catch (e) {
			status = 'Error';
		}
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

	<FileDropzone accept=".pdf" max={1} on:change={handleFileInput} />

	{#if status === 'Init' || status === 'Done'}
		<Button id="generate-button" filled round on:click={generateQuestions}>
			<div id="generate-button-text">Generate 🎲</div>
		</Button>
	{/if}
	{#if status === 'Loading'}
		<Button id="generate-button" filled round disabled>
			<div id="generate-button-text">Waiting.... OpenAI may be too busy...</div>
		</Button>
	{/if}
	{#if status === 'Error'}
		<Button id="generate-button" filled round danger on:click={generateQuestions}>
			<div id="generate-button-text">Error Please Try Again....</div>
		</Button>
	{/if}

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
