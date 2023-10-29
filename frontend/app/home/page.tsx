"use client";
import Levels from "@/components/levels";
import MicButton from "@/components/mic_button";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { useState, useEffect } from "react";

export default function Home() {
  const [returnString, setReturnString] = useState("");
  // const [onLoad, setOnLoad] = useState(true);
  const [testWord, setTestWord] = useState("");

  async function RefreshWithNewCard() {
    setTestWord("Au Revoir");
    setReturnString("");
  }

  useEffect(() => {
    //CALL MUTATE FUNC (or get api endpoint) to get a word;
    setTestWord("Bonjour");
  }, []);

  return (
    <div className="min-h-screen">
      <Card>
        <CardContent>{testWord}</CardContent>
      </Card>
      <MicButton returningString={setReturnString} word={testWord} />
      {returnString!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !==
      "" ? (
        <div>
          <Card>{returnString}</Card>
          <Button
            onClick={async () => {
              RefreshWithNewCard();
            }}
          >
            Next
          </Button>
        </div>
      ) : null}
    </div>
  );
}
