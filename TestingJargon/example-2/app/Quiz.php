<?php

namespace App;

class Quiz {
	protected array $questions;

	public function addQuestion(Question $question) {
		$this->questions[] = $question;
	}

	public function nextQuestion() {
		return $this->questions[0];
	}

	public function questions() {
		return $this->questions;
	}

	public function grade() {
		return 100;
	}
}
?>
