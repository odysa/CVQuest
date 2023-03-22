export type Status = 'Init' | 'Loading' | 'Done' | 'Error';
export type Questions = {
	technical_questions: Question[];
	behavior_questions: Question[];
};
export type Question = {
	question: string;
	answer: string;
};
