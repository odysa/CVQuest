export type Status = 'Init' | 'Loading' | 'Done';
export type Questions = {
	tech: Question[];
	behavior: Question[];
};
export type Question = {
	question: string;
	answer: string;
};
