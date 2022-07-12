<?php

namespace App;

class Question {
	protected $body;
	protected $answer;
	protected $solution;
	protected $status;

	public function __construct($body, $solution) {
		$this->body = $body;
		$this->answer = $solution;
	}

	public function answer($solution): bool {
		$this->solution = $solution;
		return $this->status = $solution === $this->answer;
	}
}
?>
