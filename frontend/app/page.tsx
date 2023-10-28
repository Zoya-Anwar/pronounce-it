"use client"
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { useState } from "react";

export default function Home() {
  const [show, setShow] = useState(true);
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-2xl font-bold pb-10">apprenons le français</h1>
      {show ? <Button className="font-bold m-2 w-24" onClick={() => setShow(!show)}> Start </Button> : null}
      {show ? null : <Card><CardContent className="font-bold p-2 m-2 w-50">Beginner</CardContent></Card>}
      {show ? null : <Card><CardContent className="font-bold p-2 m-2 w-50">Intermediate</CardContent></Card>}
      {show ? null : <Card><CardContent className="font-bold p-2 m-2 w-50">Advanced</CardContent></Card>}
    </main>
  );
}
