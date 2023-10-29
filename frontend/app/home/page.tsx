"use client";
import Levels from "@/components/levels";
import MicButton from "@/components/mic_button";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ArrowRightSquare, MoveRight } from "lucide-react";
import { useState, useEffect } from "react";
import {
  useGetWordQuery,
  ResponseData,
} from "@/hooks/query/use-get-word-query";

export default function Home() {
  const [returnString, setReturnString] = useState<JSX.Element | null>(null);
  const [testWord, setTestWord] = useState("");

  const wordQuery = useGetWordQuery({
    onSuccess(data: ResponseData) {
      console.log("success");
      setReturnString(null);
      setTestWord(data.word);
      this.enabled = false;
      this.retry = false;
    },
  });

  useEffect(() => {
    //CALL MUTATE FUNC (or get api endpoint) to get a word;
    wordQuery.refetch();
  }, [wordQuery]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-24">
      <Card className="min-w-[40vw] min-h-[20vh] flex justify-center align-middle items-center m-2">
        <CardContent className="font-black text-7xl text-center">
          {returnString !== null ? returnString : testWord}
        </CardContent>
      </Card>
      <div
        className={`flex flex-row flex-wrap content-center w-[40vw] ${
          returnString !== null ? "justify-between" : "justify-center"
        }`}
      >
        <MicButton returningString={setReturnString} word={testWord} />
        {returnString!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !==
        null ? (
          <div>
            <Button
              variant={"link"}
              className="m-2 hover:text-purple-800"
              onClick={async () => {
                wordQuery.refetch();
              }}
            >
              <MoveRight size={48} />
            </Button>
          </div>
        ) : null}
      </div>
    </div>
  );
}
