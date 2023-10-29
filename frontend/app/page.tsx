"use client";
import Levels from "@/components/levels";
import { Button } from "@/components/ui/button";
import { useState } from "react";

export default function Root() {
  const [show, setShow] = useState(true);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-2xl font-bold pb-10">apprenons le français</h1>
      <div className="flex h-5 items-center space-x-4 text-sm">
        {show ? (
          <Button className="font-bold m-2 w-24" onClick={() => setShow(!show)}>
            {" "}
            Start{" "}
          </Button>
        ) : null}
        {show ? null : <Levels />}
      </div>
    </main>
  );
}
